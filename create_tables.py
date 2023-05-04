import random

from faker import Faker
from sqlalchemy.orm import sessionmaker

from pickup_data.config import engine
from pickup_data.constants import GRADES, GENDERS, NUM_FAMILIES, STUDENTS_PER_GRADE, ITEMS
from pickup_data.models import Teacher, Family, Student, Item, Purchase

fake = Faker('en_US')


def create_teachers() -> list[Teacher]:
    teachers = []

    Session = sessionmaker(bind=engine)
    session = Session()

    for grade in GRADES + GRADES:
        gender = random.choice(GENDERS)
        first_name = fake.first_name_male() if gender == 'M' else fake.first_name_female()
        last_name = fake.last_name()

        teacher = Teacher(
            gender=gender,
            first_name=first_name,
            last_name=last_name,
            grade=grade
        )

        session.add(teacher)
        teachers.append(teacher)

    session.commit()

    for teacher in teachers:
        session.refresh(teacher)

    return teachers


def create_families() -> list[Family]:
    families = []

    Session = sessionmaker(bind=engine)
    session = Session()

    for family_num in range(NUM_FAMILIES):
        last_name = fake.last_name()
        phone_number = fake.phone_number()
        email_address = f"{last_name.lower()}@{fake.domain_name()}"

        family = Family(
            last_name=last_name,
            phone_number=phone_number,
            email_address=email_address
        )

        session.add(family)
        families.append(family)

    session.commit()

    for family in families:
        session.refresh(family)

    return families


def create_students(teachers: list[Teacher]) -> list[Student]:
    students = []

    for teacher in teachers:
        for _ in range(STUDENTS_PER_GRADE):
            gender = random.choice(GENDERS)
            first_name = fake.first_name_male() if gender == 'M' else fake.first_name_female()
            last_name = fake.last_name()
            student = Student(first_name=first_name, last_name=last_name, gender=gender, teacher_id=teacher.id)
            students.append(student)

    return students


def create_items(items: list[dict]) -> list[Item]:
    return [Item(name=item['name'], item_type=item['item_type'], price=item['price']) for item in items]


def create_purchases(students, items, num_purchases=500) -> list[Purchase]:
    purchases = []

    items_in_order = random.randint(1, 5)

    for _ in range(num_purchases):
        student = random.choice(students)
        order_id = fake.uuid4()
        purchase_timestamp = fake.date_time_this_year()

        item_set = set()
        order_id_list = []

        for i in range(items_in_order):
            item = random.choice(items)
            if item not in item_set:
                quantity = random.randint(1, 5)
                total_cost = round(item.price * quantity, 2)
                order_id_list.append(
                    Purchase(
                        purchase_timestamp=purchase_timestamp,
                        student_id=student.id,
                        order_id=order_id,
                        item_id=item.id,
                        quantity=quantity,
                        total_cost=total_cost
                    )
                )
            item_set.add(item)

        purchases.extend(order_id_list)

    return purchases


def insert_data(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    families = create_families()
    teachers = create_teachers()
    students = create_students(teachers)
    items = create_items(ITEMS)

    for student in students:
        session.add(student)
    session.commit()

    for item in items:
        session.add(item)
    session.commit()

    # Refresh the objects from the database to get the auto-incremented IDs
    for item in items:
        session.refresh(item)

    for student in students:
        session.refresh(student)

    purchases = create_purchases(students, items)
    for purchase in purchases:
        session.add(purchase)
    session.commit()

    session.close()
