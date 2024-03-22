APP = python manage.py

install: 
	pip install -r requirements.txt
	$(APP) makemigrations
	$(APP) migrate
	make install-datas

install-datas: ## Install the application
	$(APP) loaddata initialDatas/clothes_category_fixture.json
	$(APP) loaddata initialDatas/clothes_pattern_fixture.json
	$(APP) loaddata initialDatas/clothes_type_fixture.json
	$(APP) loaddata initialDatas/clothes_material_fixture.json
	$(APP) loaddata initialDatas/clothes_brand_fixture.json
	$(APP) loaddata initialDatas/account_user_fixture.json
	$(APP) loaddata initialDatas/clothes_clothing_fixture.json
	$(APP) runserver 8000

freeze: ## Freeze the requirements
	pip freeze > requirements.txt

run: ## Run the application
	$(APP) runserver 8000
	