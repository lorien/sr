from subprocess import check_output


def test_script_sr():
    out = check_output('sr', shell=True)
    assert out == b'Hello world!\n'
