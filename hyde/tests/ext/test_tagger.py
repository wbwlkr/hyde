# -*- coding: utf-8 -*-
"""
Use nose
`$ pip install nose`
`$ nosetests`
"""
from hyde.fs import File, Folder
from hyde.generator import Generator
from hyde.site import Site

from hyde.tests.util import assert_html_equals
import yaml

TEST_SITE = File(__file__).parent.parent.child_folder('_test')

class TestTagger(object):

    def setUp(self):
        TEST_SITE.make()
        TEST_SITE.parent.child_folder(
                  'sites/test_tagger').copy_contents_to(TEST_SITE)
        self.s = Site(TEST_SITE)
        self.deploy = TEST_SITE.child_folder('deploy')


    def tearDown(self):
        TEST_SITE.delete()


    def test_tagger_walker(self):
        gen = Generator(self.s)
        gen.load_site_if_needed()
        gen.generate_all()

        assert hasattr(self.s, 'tagger')
        assert hasattr(self.s.tagger, 'tags')
        assert self.s.tagger.tags
        tags = self.s.tagger.tags.to_dict()

        assert len(tags) == 5

        for tag in ['sad', 'happy', 'angry', 'thoughts', 'events']:
            assert tag in tags

        sad_posts = [post.name for post in tags['sad']]
        assert len(sad_posts) == 2
        assert "sad-post.html" in sad_posts
        assert "another-sad-post.html" in sad_posts
        sad_posts == [post.name for post in
                        self.s.content.walk_resources_tagged_with('sad')]


        happy_posts = [post.name for post in
                        self.s.content.walk_resources_tagged_with('happy')]
        assert len(happy_posts) == 1
        assert "happy-post.html" in happy_posts

        angry_posts = [post.name for post in
                        self.s.content.walk_resources_tagged_with('angry')]
        assert len(angry_posts) == 1
        assert "angry-post.html" in angry_posts

        sad_thought_posts = [post.name for post in
                        self.s.content.walk_resources_tagged_with('sad+thoughts')]
        assert len(sad_thought_posts) == 1
        assert "sad-post.html" in sad_thought_posts





    # def test_tagger_archives_generated():
    #     gen = Generator(self.s)
    #     gen.load_site_if_needed()
    #     gen.load_template_if_needed()
    #     gen.generate_all()
    #     tags_folder = self.deploy.child_folder('blog/tags')
    #
    #     blog_node = self.s.node_from_relative_path('blog')
    #     res_by_tag =
    #     for resource in blog_node.walk_resources():
    #
    #
    #     assert tags_folder.exists
    #     tags = ['sad', 'happy', 'angry', 'thoughts']
    #
    #     archives = (File(tags_folder.child("%s.html" % tag)) for tag in tags)
    #     for archive in archives:
    #         assert archive.exists
    #         assert
