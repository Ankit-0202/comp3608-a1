all:
	rm -rf __pycache__
	rm -rf */__pycache__
	rm -rf */*/__pycache__
	rm -rf */*/*/__pycache__
	rm -rf */*/*/*/__pycache__
	git add -A
	git commit -m 'Pushed'
	git push