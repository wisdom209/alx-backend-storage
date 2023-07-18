#!/usr/bin/env python3
"""pymongo script"""


def top_students(mongo_collection):
    """sort students"""
    return mongo_collection.aggregate([
        {"$project": 
            {"name": "$name", 
            "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
        ])

