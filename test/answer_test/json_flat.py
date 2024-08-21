import pytest
from gendiff import gen_diff


def test_same_files():
    file1 = 'test/fixtures/file1.json'
    file2 = 'test/fixtures/file1.json'
    result = '''{
follow: false
host: hexlet.io
proxy: 123.234.53.22
timeout: 50
}'''
    assert gen_diff(file1, file2) == result


def test_different_files():
    file1 = 'test/fixtures/file1.json'
    file2 = 'test/fixtures/file2.json'
    result = '''{
- follow: false
host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}'''
    assert gen_diff(file1, file2) == result


def test_empty_files():
    file1 = 'test/fixtures/empty.json'
    file2 = 'test/fixtures/empty.json'
    result = '{}'
    assert gen_diff(file1, file2) == result


def test_empty_and_full():
    file1 = 'test/fixtures/file1.json'
    file2 = 'test/fixtures/empty.json'
    result = '''{
- follow: false
- host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
}'''
    assert gen_diff(file1, file2) == result
