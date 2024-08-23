import pytest
from gendiff import gen_diff


@pytest.mark.parametrize("file1, file2, expected_result", [
    ("tests/fixtures/file1.json", "tests/fixtures/file1.json", '''{
follow: false
host: hexlet.io
proxy: 123.234.53.22
timeout: 50
}'''),
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", '''{
- follow: false
host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}'''),
    ("tests/fixtures/empty.json", "tests/fixtures/empty.json", '{}'),
    ("tests/fixtures/file1.json", "tests/fixtures/empty.json", '''{
- follow: false
- host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
}''')])
def test_diff(file1, file2, expected_result):
    actual_result = gen_diff(file1, file2)
    assert actual_result == expected_result
