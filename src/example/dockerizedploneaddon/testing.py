# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import example.dockerizedploneaddon


class ExampleDockerizedploneaddonLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=example.dockerizedploneaddon)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'example.dockerizedploneaddon:default')


EXAMPLE_DOCKERIZEDPLONEADDON_FIXTURE = ExampleDockerizedploneaddonLayer()


EXAMPLE_DOCKERIZEDPLONEADDON_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EXAMPLE_DOCKERIZEDPLONEADDON_FIXTURE,),
    name='ExampleDockerizedploneaddonLayer:IntegrationTesting',
)


EXAMPLE_DOCKERIZEDPLONEADDON_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EXAMPLE_DOCKERIZEDPLONEADDON_FIXTURE,),
    name='ExampleDockerizedploneaddonLayer:FunctionalTesting',
)


EXAMPLE_DOCKERIZEDPLONEADDON_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EXAMPLE_DOCKERIZEDPLONEADDON_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ExampleDockerizedploneaddonLayer:AcceptanceTesting',
)
