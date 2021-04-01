def add(a,b):
	return a + b

def test_add():
	assert add(0.1,0.2) - 0.3 < 1e-06
	assert add('space', 'ship') == 'spaceship'