# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-20 15:39
from __future__ import unicode_literals

from django.db import migrations


def delete_parent_sectors(apps, schema_editor):
    ParentSector = apps.get_model('mi', 'ParentSector')
    ParentSector.objects.all().delete()

def add_parent_sectors(apps, schema_editor):
    ParentSector = apps.get_model('mi', 'ParentSector')
    SectorTeam = apps.get_model('mi', 'SectorTeam')

    parent_sectors = {
        1: "Advanced Engineering",
        2: "Aerospace",
        3: "Agriculture, Horticulture and Fisheries",
        4: "Airports",
        5: "Automotive",
        6: "Biotechnology and Pharmaceuticals",
        7: "Business (and Consumer) Services",
        8: "Chemicals",
        9: "Clothing, Footwear and Fashion",
        10: "Communications",
        11: "Construction",
        12: "Creative and Media",
        13: "Defence",
        14: "Defence and Security",
        15: "Education and Training",
        16: "Electronics and IT Hardware",
        17: "Energy",
        18: "Environment",
        19: "Environment and Water",
        20: "Financial Services (including Professional Services)",
        21: "Food and Drink",
        22: "Giftware, Jewellery and Tableware",
        23: "Global Sports Projects",
        24: "Healthcare and Medical",
        25: "Household Goods, Furniture and Furnishings",
        26: "ICT",
        27: "Leisure and Tourism",
        28: "Life Sciences",
        29: "Marine",
        30: "Mass Transport",
        31: "Mechanical Electrical and Process Engineering",
        32: "Metallurgical Process Plant",
        33: "Metals, Minerals and Materials",
        34: "Mining",
        35: "Oil and Gas",
        36: "Ports and Logistics",
        37: "Power",
        38: "Railways",
        39: "Renewable Energy",
        40: "Retail",
        41: "Security",
        42: "Software and Computer Services Business to Business (B2B)",
        43: "Textiles, Interior Textiles and Carpets",
        44: "Water"
    }
    parent_sector_to_sector_team = {
        "Advanced Engineering": "Advanced Manufacturing",
        "Aerospace": "Aerospace",
        "Agriculture, Horticulture and Fisheries": "Bio-economy",
        "Airports": "Infrastructure",
        "Automotive": "Automotive",
        "Biotechnology and Pharmaceuticals": "Life Sciences",
        "Business (and Consumer) Services": "Financial & Professional Services",
        "Chemicals": "Bio-economy",
        "Clothing, Footwear and Fashion": "Consumer & Creative",
        "Communications": "Technology",
        "Construction": "Infrastructure",
        "Creative and Media": "Consumer & Creative",
        "Defence": "Defence & Security",
        "Defence and Security": "Defence & Security",
        "Education and Training": "Education",
        "Electronics and IT Hardware": "Technology",
        "Energy": "Energy",
        "Environment": "Infrastructure",
        "Environment and Water": "Infrastructure",
        "Financial Services (including Professional Services)": "Financial & Professional Services",
        "Food and Drink": "Food & Drink",
        "Giftware, Jewellery and Tableware": "Consumer & Creative",
        "Global Sports Projects": "Consumer & Creative",
        "Healthcare and Medical": "Healthcare",
        "Household Goods, Furniture and Furnishings": "Consumer & Creative",
        "ICT": "Technology",
        "Leisure and Tourism": "Consumer & Creative",
        "Life Sciences": "Life Sciences",
        "Marine": "Advanced Manufacturing",
        "Mass Transport": "Infrastructure",
        "Mechanical Electrical and Process Engineering": "Advanced Manufacturing",
        "Metallurgical Process Plant": "Advanced Manufacturing",
        "Metals, Minerals and Materials": "Infrastructure",
        "Mining": "Infrastructure",
        "Oil and Gas": "Energy",
        "Ports and Logistics": "Infrastructure",
        "Power": "Energy",
        "Railways": "Infrastructure",
        "Renewable Energy": "Energy",
        "Retail": "Consumer & Creative",
        "Security": "Defence & Security",
        "Software and Computer Services Business to Business (B2B)": "Technology",
        "Textiles, Interior Textiles and Carpets": "Consumer & Creative",
        "Water": "Infrastructure"
    }

    for parent_id, parent_name in parent_sectors.items():
        team = parent_sector_to_sector_team[parent_name]
        sector_team = SectorTeam.objects.get(name=team)
        ParentSector(id=parent_id, name=parent_name, sector_team=sector_team).save()


class Migration(migrations.Migration):

    dependencies = [
        ('mi', '0021_auto_20170120_1253'),
    ]

    operations = [
        migrations.RunPython(delete_parent_sectors),
        migrations.RunPython(add_parent_sectors),
    ]