# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import example.async


class ExampleAsyncLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=example.async)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'example.async:default')


EXAMPLE_ASYNC_FIXTURE = ExampleAsyncLayer()


EXAMPLE_ASYNC_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EXAMPLE_ASYNC_FIXTURE,),
    name='ExampleAsyncLayer:IntegrationTesting'
)


EXAMPLE_ASYNC_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EXAMPLE_ASYNC_FIXTURE,),
    name='ExampleAsyncLayer:FunctionalTesting'
)


EXAMPLE_ASYNC_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EXAMPLE_ASYNC_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ExampleAsyncLayer:AcceptanceTesting'
)
