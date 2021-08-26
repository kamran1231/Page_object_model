import pytest

from pytest_mock import MockFixture
from pytest_ast_transformer.ast_manager import ASTManager

pytest_plugins = ["pytester"]


@pytest.fixture
def mocker(pytestconfig):
    result = MockFixture(pytestconfig)
    yield result
    result.stopall()


from examples.experements import transformer


def pytest_register_ast_transformer(ast_manager: ASTManager):
    ast_manager.add_transformer(transformer.AssertTransformer())
    ast_manager.add_transformer(transformer.FunctionsToAssertTransformer())
    # ast_manager.add_transformer(transformer.AssertTransformer2())
