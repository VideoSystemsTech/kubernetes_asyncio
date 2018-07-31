# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.11.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.admissionregistration_v1alpha1_api import AdmissionregistrationV1alpha1Api  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestAdmissionregistrationV1alpha1Api(unittest.TestCase):
    """AdmissionregistrationV1alpha1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.admissionregistration_v1alpha1_api.AdmissionregistrationV1alpha1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_initializer_configuration(self):
        """Test case for create_initializer_configuration

        """
        pass

    def test_delete_collection_initializer_configuration(self):
        """Test case for delete_collection_initializer_configuration

        """
        pass

    def test_delete_initializer_configuration(self):
        """Test case for delete_initializer_configuration

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_initializer_configuration(self):
        """Test case for list_initializer_configuration

        """
        pass

    def test_patch_initializer_configuration(self):
        """Test case for patch_initializer_configuration

        """
        pass

    def test_read_initializer_configuration(self):
        """Test case for read_initializer_configuration

        """
        pass

    def test_replace_initializer_configuration(self):
        """Test case for replace_initializer_configuration

        """
        pass


if __name__ == '__main__':
    unittest.main()
