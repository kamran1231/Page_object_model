import ast
# import astunparse

from pytest_ast_transformer.transformer import PytestTransformer


def my_assert(test_result, msg):
    print(f'my assert: {test_result} {msg}')
    assert test_result, msg


def my_kek(*args, **kwargs):
    raise Exception('Ti pidor')


class AssertTransformer(PytestTransformer):
    context = {
        'my_assert': my_assert
    }

    def visit_Assert(self, node: ast.Assert) -> ast.Expr:
        func_name = ast.Name(id='my_assert', ctx=ast.Load())
        call_func = ast.Call(func=func_name, args=[node.test, node.msg], keywords=[])
        expr = ast.Expr(value=call_func)

        return ast.fix_missing_locations(expr)


class AssertTransformer2(PytestTransformer):
    context = {
        'my_kek': my_kek
    }

    def visit_Assert(self, node: ast.Assert) -> ast.Expr:
        func_name = ast.Name(id='my_kek', ctx=ast.Load())
        call_func = ast.Call(func=func_name, args=[node.test, node.msg], keywords=[])
        expr = ast.Expr(value=call_func)

        return ast.fix_missing_locations(expr)


class FunctionsToAssertTransformer(PytestTransformer):
    allow_inheritance_ctx = True
    context = {}

    def visit_FunctionDef(self, node: ast.FunctionDef):
        test = ast.Compare(
            left=ast.Num(n=155),
            ops=[ast.Eq()],
            comparators=[ast.Num(n=2)]
        )
        msg = ast.Str(s='ny kek')
        assert_ = ast.Assert(test=test, msg=msg)

        func_name = ast.Name(id='my_assert', ctx=ast.Load())
        call_func = ast.Call(func=func_name, args=[assert_.test, assert_.msg], keywords=[])
        expr = ast.Expr(value=call_func)

        node.body.append(expr)

        return node

    # def visit_ClassDef(self, node: ast.FunctionDef):
    #     node_func = node.body[0]
    #     test = ast.Compare(
    #         left=ast.Num(n=155),
    #         ops=[ast.Eq()],
    #         comparators=[ast.Num(n=2)]
    #     )
    #     msg = ast.Str(s='ny kek')
    #     assert_ = ast.Assert(test=test, msg=msg)
    #
    #     func_name = ast.Name(id='my_assert', ctx=ast.Load())
    #     call_func = ast.Call(func=func_name, args=[assert_.test, assert_.msg], keywords=[])
    #     assert_ = ast.Expr(value=call_func)
    #
    #     new_body = [*node_func.body, assert_]
    #
    #     func = ast.FunctionDef(
    #         name=node_func.name,
    #         args=node_func.args,
    #         returns=node_func.returns,
    #         body=new_body,
    #         decorator_list=node_func.decorator_list,
    #     )
    #
    #     new_funcs = [*node.body, func]
    #
    #     cls = ast.ClassDef(
    #         name=node.name,
    #         bases=node.bases,
    #         keywords=node.keywords,
    #         body=new_funcs,
    #         decorator_list=node.decorator_list,
    #     )
    #
    #     new_node = ast.parse(astunparse.unparse(cls))
    #     new_node = new_node.body[0]
    #
    #     return new_node

    # def visit_Expr(self, node: ast.Expr) -> ast.Expr:
    #     if (
    #             isinstance(node.value, ast.Call)
    #             and node.value.func.id == 'my_assert'
    #     ):
    #         test, msg = node.value.args
    #         assert_ = ast.Assert(test=test, msg=msg)
    #
    #         return ast.fix_missing_locations(assert_)
    #
    #     return self.generic_visit(node)
