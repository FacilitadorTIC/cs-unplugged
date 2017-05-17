"""Create test data for topic tests."""

import os.path
import yaml

from topics.models import (
    Topic,
    UnitPlan,
    Lesson,
    CurriculumIntegration,
    CurriculumArea,
    ProgrammingExercise,
    ProgrammingExerciseDifficulty,
    ProgrammingExerciseLanguage,
    LearningOutcome,
)


class TopicsTestDataGenerator:
    """Class for generating test data for topics."""

    def __init__(self):
        """Create TopicsTestDataGenerator object."""
        self.BASE_PATH = "tests/topics/"
        self.LOADER_ASSET_PATH = os.path.join(self.BASE_PATH, "loaders/assets/")

    def load_yaml_file(self, yaml_file_path):
        """Load a yaml file.

        Args:
            yaml_file_path:  The path to a given yaml file (str).

        Returns:
            Contents of a yaml file.
        """
        yaml_file = open(yaml_file_path, encoding="UTF-8").read()
        return yaml.load(yaml_file)

    def create_integration(self, topic, number, lessons=None, curriculum_areas=None):
        """Create curriculum integration object.

        Args:
            topic: The related Topic object.
            number: Integer representing the topic.
            lessons: List of prerequisite lessons.
            curriculum_areas: List of curriculum areas.

        Returns:
            CurriculumIntegration object.
        """
        integration = CurriculumIntegration(
            topic=topic,
            slug="integration-{}".format(number),
            name="Integration {}".format(number),
            number=number,
            content="<p>Content for integration {}.</p>".format(number),
        )
        integration.save()
        if lessons:
            for lesson in lessons:
                integration.prerequisite_lessons.add(lesson)
        if curriculum_areas:
            for curriculum_area in curriculum_areas:
                integration.curriculum_areas.add(curriculum_area)
        return integration

    def create_curriculum_area(self, number, parent=None):
        """Create curriculum area object.

        Args:
            number: Integer representing the area.
            parent: Parent of the curriculum area.

        Returns:
            CurriculumArea object.
        """
        area = CurriculumArea(
            slug="area-{}".format(number),
            name="Area {}".format(number),
            parent=parent,
        )
        area.save()
        return area

    def create_topic(self, number):
        """Create topic object.

        Args:
            number: Integer representing the topic.

        Returns:
            Topic object.
        """
        topic = Topic(
            slug="topic-{}".format(number),
            name="Topic {}".format(number),
            content="<p>Content for topic {}.</p>".format(number),
        )
        topic.save()
        return topic

    def create_unit_plan(self, topic, number):
        """Create unit plan object.

        Args:
            topic: The related Topic object.
            number: Integer representing the unit plan.

        Returns:
            UnitPlan object.
        """
        unit_plan = UnitPlan(
            topic=topic,
            slug="unit-plan-{}".format(number),
            name="Unit Plan {}".format(number),
            content="<p>Content for unit plan {}.</p>".format(number),
        )
        unit_plan.save()
        return unit_plan

    def create_lesson(self, topic, unit_plan, number, min_age, max_age):
        """Create lesson object.

        Args:
            topic: The related Topic object.
            unit_plan: The related UnitPlan object.
            number: Integer representing the topic.
            min_age: Integer of the minimum age of the lesson.
            max_age: Integer of the maximum age of the lesson.

        Returns:
            Lesson object.
        """
        lesson = Lesson(
            topic=topic,
            unit_plan=unit_plan,
            slug="lesson-{}".format(number),
            name="Lesson {} ({} to {})".format(number, min_age, max_age),
            number=number,
            duration=number,
            content="<p>Content for lesson {}.</p>".format(number),
            min_age=min_age,
            max_age=max_age,
        )
        lesson.save()
        return lesson

    def create_difficulty_level(self, number):
        """
        Create difficuly level object.

        Args:
            number: Integer representing the level.

        Returns:
            ProgrammingExerciseDifficulty object.
        """
        difficulty = ProgrammingExerciseDifficulty(
            level="1",
            name="Difficulty-{}".format(number)
        )
        difficulty.save()
        return difficulty

    def create_programming_language(self, number):
        """
        Create programming language object.

        Args:
            number: Integer representing the language.

        Returns:
            ProgrammingExerciseLanguage object.
        """
        language = ProgrammingExerciseLanguage(
            slug="language-{}".format(number),
            name="Language {}".format(number),
        )
        language.save()
        return language

    def create_programming_exercise(self, topic, number,
                                    difficulty,
                                    exercise_set_number=1,
                                    exercise_number=1,
                                    content="<p>Example content.</p>",
                                    extra_challenge="<p>Example challenge.</p>",
                                    ):
        """
        Create programming exercise object.

        Args:
            topic: Topic related to the exercise.
            number: Integer representing the exercise (int).
            difficulty: Difficulty related to the exercise.
            exercise_set_number: Integer of exercise set number (int).
            exercise_number: Integer of exercise number (int).
            content: Text of exercise (str).
            extra_challenge: Text of extra challenge (str).

        Returns:
            ProgrammingExercise object.
        """
        exercise = ProgrammingExercise(
            topic=topic,
            slug="exercise-{}".format(number),
            name="Exercise {}".format(number),
            exercise_set_number=exercise_set_number,
            exercise_number=exercise_number,
            content=content,
            extra_challenge=extra_challenge,
            difficulty=difficulty,
        )
        exercise.save()
        return exercise

    def create_learning_outcome(self, number):
        """
        Create learning outcome object.

        Args:
            number: Integer representing the exercise (int).

        Returns:
            LearningOutcome object.
        """
        outcome = LearningOutcome(
            slug="outcome-{}".format(number),
            text="Outcome {}".format(number),
        )
        outcome.save()
        return outcome
