#!/usr/bin/env python3
"""Schools by topic"""


def schools_by_topic(mongo_collection, topic):
    """Find schools by topic"""
    return list(mongo_collection.find({"topics": topic}))
