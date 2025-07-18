# coding: utf-8

"""
    Graphiant APIs

    Graphiant API documentation.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from graphiant_sdk.models.v2_assistant_add_to_conversation_post200_response_dataframe_dictionary_inner import V2AssistantAddToConversationPost200ResponseDataframeDictionaryInner
from graphiant_sdk.models.v2_assistant_add_to_conversation_post_request_question import V2AssistantAddToConversationPostRequestQuestion
from typing import Optional, Set
from typing_extensions import Self

class V2AssistantAddToConversationPost200Response(BaseModel):
    """
    V2AssistantAddToConversationPost200Response
    """ # noqa: E501
    conversation_id: Optional[StrictStr] = Field(default=None, alias="conversationId")
    dataframe_dictionary: Optional[List[V2AssistantAddToConversationPost200ResponseDataframeDictionaryInner]] = Field(default=None, alias="dataframeDictionary")
    original_question: Optional[V2AssistantAddToConversationPostRequestQuestion] = Field(default=None, alias="originalQuestion")
    response_id: Optional[StrictStr] = Field(default=None, alias="responseId")
    response_language: Optional[StrictStr] = Field(default=None, alias="responseLanguage")
    response_text: Optional[StrictStr] = Field(default=None, alias="responseText")
    response_timestamp: Optional[StrictInt] = Field(default=None, alias="responseTimestamp")
    response_type: Optional[StrictStr] = Field(default=None, alias="responseType")
    __properties: ClassVar[List[str]] = ["conversationId", "dataframeDictionary", "originalQuestion", "responseId", "responseLanguage", "responseText", "responseTimestamp", "responseType"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V2AssistantAddToConversationPost200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in dataframe_dictionary (list)
        _items = []
        if self.dataframe_dictionary:
            for _item_dataframe_dictionary in self.dataframe_dictionary:
                if _item_dataframe_dictionary:
                    _items.append(_item_dataframe_dictionary.to_dict())
            _dict['dataframeDictionary'] = _items
        # override the default output from pydantic by calling `to_dict()` of original_question
        if self.original_question:
            _dict['originalQuestion'] = self.original_question.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2AssistantAddToConversationPost200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conversationId": obj.get("conversationId"),
            "dataframeDictionary": [V2AssistantAddToConversationPost200ResponseDataframeDictionaryInner.from_dict(_item) for _item in obj["dataframeDictionary"]] if obj.get("dataframeDictionary") is not None else None,
            "originalQuestion": V2AssistantAddToConversationPostRequestQuestion.from_dict(obj["originalQuestion"]) if obj.get("originalQuestion") is not None else None,
            "responseId": obj.get("responseId"),
            "responseLanguage": obj.get("responseLanguage"),
            "responseText": obj.get("responseText"),
            "responseTimestamp": obj.get("responseTimestamp"),
            "responseType": obj.get("responseType")
        })
        return _obj


