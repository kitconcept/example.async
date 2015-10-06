# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from example.async.testing import EXAMPLE_ASYNC_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that example.async is properly installed."""

    layer = EXAMPLE_ASYNC_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if example.async is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('example.async'))

    def test_browserlayer(self):
        """Test that IExampleAsyncLayer is registered."""
        from example.async.interfaces import IExampleAsyncLayer
        from plone.browserlayer import utils
        self.assertIn(IExampleAsyncLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EXAMPLE_ASYNC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['example.async'])

    def test_product_uninstalled(self):
        """Test if example.async is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('example.async'))
