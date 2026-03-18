import math

from django.shortcuts import render


def classes_needed_for_target(total_classes, attended_classes, target=75):
    if total_classes <= 0:
        return 0

    percentage = (attended_classes / total_classes) * 100
    if percentage >= target:
        return 0

    required_classes = ((target / 100) * total_classes - attended_classes) / (1 - (target / 100))
    return max(0, math.ceil(required_classes))


def home(request):
    context = {"has_result": False}

    if request.method == "POST":
        total_classes_raw = request.POST.get("total_classes", "").strip()
        attended_classes_raw = request.POST.get("attended_classes", "").strip()

        context["total_classes"] = total_classes_raw
        context["attended_classes"] = attended_classes_raw

        try:
            total_classes = int(total_classes_raw)
            attended_classes = int(attended_classes_raw)

            if total_classes <= 0:
                context["error"] = "Total classes must be greater than 0."
            elif attended_classes < 0:
                context["error"] = "Attended classes cannot be negative."
            elif attended_classes > total_classes:
                context["error"] = "Attended classes cannot be greater than total classes."
            else:
                percentage = (attended_classes / total_classes) * 100
                needed_classes = classes_needed_for_target(total_classes, attended_classes)
                target_total_classes = total_classes + needed_classes
                target_attended_classes = attended_classes + needed_classes
                target_percentage = (target_attended_classes / target_total_classes) * 100
                status = "Safe Attendance" if percentage >= 75 else "Low Attendance Warning"
                context["percentage"] = round(percentage, 2)
                context["percentage_display"] = f"{percentage:.2f}"
                context["status"] = status
                context["needed_classes"] = needed_classes
                context["target_total_classes"] = target_total_classes
                context["target_attended_classes"] = target_attended_classes
                context["target_percentage"] = round(target_percentage, 2)
                context["target_percentage_display"] = f"{target_percentage:.2f}"
                context["current_attendance_text"] = (
                    f"Current Attendance: {attended_classes}/{total_classes} -> {percentage:.2f}%"
                )
                context["required_attendance_text"] = (
                    f"Attendance Required: {target_attended_classes}/{target_total_classes} -> {target_percentage:.2f}%"
                )
                context["has_result"] = True
        except ValueError:
            context["error"] = "Please enter valid whole numbers."

    return render(request, "home.html", context)
