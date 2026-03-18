from django.test import TestCase
from django.urls import reverse

from calculator.views import classes_needed_for_target


class ClassesNeededForTargetTests(TestCase):
    def test_calculates_needed_classes_for_given_example(self):
        self.assertEqual(classes_needed_for_target(251, 136), 209)

    def test_returns_zero_when_attendance_already_meets_target(self):
        self.assertEqual(classes_needed_for_target(100, 75), 0)


class HomeViewTests(TestCase):
    def test_post_renders_expected_recovery_plan_for_given_example(self):
        response = self.client.post(
            reverse("home"),
            {"total_classes": "251", "attended_classes": "136"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "You need to attend 209 more classes to attain 75% attendance.",
        )
        self.assertContains(
            response,
            "Current Attendance: 136/251 -&gt; 54.18%",
        )
        self.assertContains(
            response,
            "Attendance Required: 345/460 -&gt; 75.00%",
        )

    def test_post_shows_requirement_already_met_when_safe(self):
        response = self.client.post(
            reverse("home"),
            {"total_classes": "100", "attended_classes": "80"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "You already meet the 75% attendance requirement.",
        )
