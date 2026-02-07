#!/usr/bin/env python3
"""
101-students.py - Function to get top students by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    
    Args:
        mongo_collection: pymongo collection object
        
    Returns:
        List of students with averageScore added, sorted by averageScore desc
    """
    pipeline = [
        {
            "$unwind": "$topics"  # Separa cada tema en un documento
        },
        {
            "$group": {
                "_id": "$_id",  # Agrupa por estudiante
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}  # Calcula promedio
            }
        },
        {
            "$sort": {"averageScore": -1}  # Ordena descendente
        },
        {
            "$project": {  # Reestructura el documento
                "_id": 1,
                "name": 1,
                "averageScore": 1
            }
        }
    ]
    
    return list(mongo_collection.aggregate(pipeline))
