from model_mommy import mommy

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import (
    CurriculumIntegration,
    CurriculumArea,
    Lesson
)


class CurriculumIntegrationModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()

    def test_curriculum_integration(self):
        # Setup Auxliary Data
        topic = self.test_data.create_topic(1)
        curriculum_area = mommy.make(
            CurriculumArea,
            name="cats"
        )
        prerequisite_lesson = mommy.make(
            Lesson,
            name="dogs"
        )
        new_curriculum_integration = CurriculumIntegration.objects.create(
            topic=topic,
            slug="slug",
            number=1,
            name="name",
            content="content"
        )
        new_curriculum_integration.curriculum_areas.add(curriculum_area)
        new_curriculum_integration.prerequisite_lessons.add(prerequisite_lesson)

        query_result = CurriculumIntegration.objects.get(slug="slug")
        self.assertEqual(query_result, new_curriculum_integration)
