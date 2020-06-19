import pytest

from DictPathImmutable import Dict_Path_Immutable


class TestDictPathImmutable:
    def testGet(self):
        test_encounter_data = {
            "cardSurgInfo": {"hamAndSwiss": {"value": 1, "label": "Yes Please"}},
            "DOB": "01/11/1991",
            "isHungry": True,
            "isNamedAlex": True,
            "sampleArrayifiedField": [
                {"turkeyAndProvaloneInfo": {"isToasted": {"value": 1, "label": "Yes"}}},
                {"turkeyAndProvaloneInfo": {"isToasted": {"value": 0, "label": "No"}}},
            ],
        }

        value = Dict_Path_Immutable.get(
            test_encounter_data,
            "sampleArrayifiedField.0.turkeyAndProvaloneInfo.isToasted.value",  # PATH TO VALUE
        )

        assert value == 1

        value = Dict_Path_Immutable.get(
            test_encounter_data,
            "sampleArrayifiedField.0.turkeyAndProvaloneInfo.isToasted.i_do_not_exist",  # PATH TO VALUE
        )

        assert value == None

    def testSet(self):
        test_encounter_data = {
            "cardSurgInfo": {"hamAndSwiss": {"value": 1, "label": "Yes Please"}},
            "DOB": "01/11/1991",
            "isHungry": True,
            "isNamedAlex": True,
            "sampleArrayifiedField": [
                {"turkeyAndProvaloneInfo": {"isToasted": {"value": 1, "label": "Yes"}}},
                {"turkeyAndProvaloneInfo": {"isToasted": {"value": 0, "label": "No"}}},
            ],
        }

        postSet = Dict_Path_Immutable.set(
            test_encounter_data,
            "cardSurgInfo.hamAndSwiss",  # PATH TO VALUE
            {"value": 0, "label": "No Thank you"},
        )

        postSet = Dict_Path_Immutable.set(
            postSet,
            "sampleArrayifiedField.1.turkeyAndProvaloneInfo.isToasted",  # PATH TO VALUE
            {"value": 1, "label": "Yes"},
        )

        postSet = Dict_Path_Immutable.set(
            postSet,
            "sampleArrayifiedField.2.turkeyAndProvaloneInfo.isToasted",  # PATH TO VALUE
            {"value": 1, "label": "Yes"},
        )

        assert postSet["cardSurgInfo"]["hamAndSwiss"]["value"] == 0
        assert (
            postSet["sampleArrayifiedField"][1]["turkeyAndProvaloneInfo"]["isToasted"][
                "value"
            ]
            == 1
        )
        assert (
            postSet["sampleArrayifiedField"][2]["turkeyAndProvaloneInfo"]["isToasted"][
                "value"
            ]
            == 1
        )

    def testDelete(self):
        test_encounter_data = {
            "cardSurgInfo": {"hamAndSwiss": {"value": 1, "label": "Yes Please"}},
            "DOB": "01/11/1991",
            "isHungry": True,
            "isNamedAlex": True,
            "sampleArrayifiedField": [
                {"turkeyAndProvaloneInfo": {"isToasted": {"value": 1, "label": "Yes"}}},
                {"turkeyAndProvaloneInfo": {"isToasted": {"value": 0, "label": "No"}}},
            ],
        }

        postDelete = Dict_Path_Immutable.delete(
            test_encounter_data, "cardSurgInfo.hamAndSwiss"
        )

        postDelete = Dict_Path_Immutable.delete(
            postDelete, "sampleArrayifiedField.1.turkeyAndProvaloneInfo.isToasted"
        )

        postDelete = Dict_Path_Immutable.delete(postDelete, "DOB2")

        assert postDelete["cardSurgInfo"] == {}
        assert postDelete["sampleArrayifiedField"][1]["turkeyAndProvaloneInfo"] == {}
        assert len(postDelete.keys()) == 5
