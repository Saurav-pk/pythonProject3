def individual_serial(student) -> dict:
    return {
        "id": str(student["_id"]),
        "student_id": student["student_id"],
        "student_name": student["student_name"],
        "department": student["department"],
        "phone_number": student["phone_number"],
        "address": student["address"]
    }

def list_serial(students) -> list:
    return [individual_serial(student) for student in students]
