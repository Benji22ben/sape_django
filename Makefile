APP = python manage.py
DOCKER_EXEC = docker exec sape_django

install: 
	$(DOCKER_EXEC) $(APP) makemigrations account
	$(DOCKER_EXEC) $(APP) makemigrations clothes
	$(DOCKER_EXEC) $(APP) makemigrations 
	$(DOCKER_EXEC) $(APP) migrate account
	$(DOCKER_EXEC) $(APP) migrate clothes
	$(DOCKER_EXEC) $(APP) migrate
	make install-datas

install-datas: ## Install the application
	$(DOCKER_EXEC) $(APP) loaddata initialDatas/clothes_category_fixture.json
	$(DOCKER_EXEC) $(APP) loaddata initialDatas/clothes_pattern_fixture.json
	$(DOCKER_EXEC) $(APP) loaddata initialDatas/clothes_type_fixture.json
	$(DOCKER_EXEC) $(APP) loaddata initialDatas/clothes_material_fixture.json
	$(DOCKER_EXEC) $(APP) loaddata initialDatas/clothes_brand_fixture.json
	$(DOCKER_EXEC) $(APP) loaddata initialDatas/account_user_fixture.json
	$(DOCKER_EXEC) $(APP) loaddata initialDatas/clothes_clothing_fixture.json

freeze: ## Freeze the requirements
	pip freeze > requirements.txt

run: ## Run the application
	$(APP) runserver 8000
	
migration: ## Create a migration
	$(APP) makemigrations
	$(APP) migrate

up:
	docker compose up -d

down:
	docker compose down