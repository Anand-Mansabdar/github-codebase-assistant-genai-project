from retrieval.context_builder import (
    MultiFileContextBuilder,
)
from retrieval.models import SearchResult


def test_context_builder_groups_files():

    results = [
        SearchResult(
            content="def authenticate(): pass",
            source_file="auth.py",
            language="Python",
            start_line=10,
            end_line=10,
            class_name=None,
            function_name="authenticate",
            distance=0.1,
            score=0.9,
        ),
        SearchResult(
            content="def login(): pass",
            source_file="api.py",
            language="Python",
            start_line=20,
            end_line=20,
            class_name=None,
            function_name="login",
            distance=0.2,
            score=0.8,
        ),
    ]

    builder = MultiFileContextBuilder()

    context = builder.build(results)
    
    print("=" * 80)
    print("GENERATED CONTEXT")
    print("=" * 80)
    print(context)
    print("=" * 80)

    assert "FILE: auth.py" in context
    assert "FILE: api.py" in context

    assert "authenticate" in context
    assert "login" in context