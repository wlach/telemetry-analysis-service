import factory

from django.contrib.auth.models import User, Group


class GroupFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Group #%s" % n)

    class Meta:
        model = Group


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user%s' % n)
    first_name = factory.Sequence(lambda n: "user %03d" % n)
    email = 'test@example.com'
    password = factory.PostGenerationMethodCall('set_password', 'password')

    class Meta:
        model = User

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.groups.add(group)
