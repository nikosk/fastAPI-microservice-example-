#!/usr/bin/env bash

migrate_test_db() {
  echo "Migrating test db"
  export DATABASE_URL="sqlite:tests/test.db"
  dbmate -d ./migrations up
  unset DATABASE_URL
}

if [ -z "$1" ]; then
  echo "No argument supplied"
else
  if [ $1 = "watch" ]; then
    echo "Running app with reload"
    export CONFIG_FILE="app/.env" && uvicorn app.main:app --reload
    exit
  elif [ $1 = "migrate" ]; then
    echo "Migrating"
    export DATABASE_URL="sqlite:user.db"
    dbmate -d ./migrations up
    unset DATABASE_URL
  elif [ $1 = "test" ]; then
    migrate_test_db
    cd tests
    export CONFIG_FILE=".env" && pytest
    rm test.db
    unset CONFIG_FILE
    cd ..
  elif [ $1 = "testdb" ]; then
    migrate_test_db
  fi
fi


