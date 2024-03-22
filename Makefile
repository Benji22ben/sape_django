APP = python manage.py


install: ## Install the application
	$(APP) loaddata initialDatas/clothes_category_fixture.json
	$(APP) loaddata initialDatas/clothes_pattern_fixture.json
	$(APP) loaddata initialDatas/clothes_type_fixture.json
	$(APP) loaddata initialDatas/clothes_material_fixture.json
	$(APP) loaddata initialDatas/clothes_brand_fixture.json
	$(APP) loaddata initialDatas/account_user_fixture.json
	$(APP) loaddata initialDatas/clothes_clothing_fixture.json
	$(APP) runserver 8000