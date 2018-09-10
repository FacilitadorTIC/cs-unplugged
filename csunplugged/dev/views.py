"""Views for the dev application."""

from django.views import generic
from utils.group_lessons_by_age import group_lessons_by_age
from topics.models import (
    Topic,
    CurriculumArea,
    CurriculumIntegration,
    ProgrammingChallenge,
    ProgrammingChallengeDifficulty,
    ProgrammingChallengeLanguage,
    LearningOutcome,
    GlossaryTerm,
)


class IndexView(generic.TemplateView):
    """View for the dev application homepage."""

    template_name = "dev/index.html"
    context_object_name = "all_topics"

    def get_context_data(self, **kwargs):
        """Return context for dev homepage.

        Returns:
            A dictionary of context data.
        """
        context = super(IndexView, self).get_context_data(**kwargs)

        # Get topic, unit plan and lesson lists
        context["topics"] = Topic.objects.order_by("name")

        # Build dictionaries for each unit plan and lesson
        for topic in context["topics"]:
            unit_plans = []
            for unit_plan in topic.unit_plans.all():
                unit_plan.grouped_lessons = group_lessons_by_age(unit_plan.lessons.all())
                unit_plans.append(unit_plan)
            topic.units = unit_plans
            topic.integrations = CurriculumIntegration.objects.filter(topic=topic).order_by("number")
            topic.programming_challenges = ProgrammingChallenge.objects.filter(topic=topic).order_by(
                "challenge_set_number", "challenge_number"
            )

        # Get curriculum area list
        context["curriculum_areas"] = []
        for parent in CurriculumArea.objects.filter(parent=None).order_by("name"):
            children = list(CurriculumArea.objects.filter(parent=parent).order_by("name"))
            context["curriculum_areas"].append((parent, children))

        # Get learning outcome list
        context["learning_outcomes"] = LearningOutcome.objects.all()

        # Get learning outcome list
        context["programming_challenge_languages"] = ProgrammingChallengeLanguage.objects.all()

        # Get learning outcome list
        context["programming_challenge_difficulties"] = ProgrammingChallengeDifficulty.objects.all()

        # Get glossary term list
        context["glossary_terms"] = GlossaryTerm.objects.all().order_by("term")

        return context
