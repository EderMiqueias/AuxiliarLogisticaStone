# AuxiliarLogisticaStone

## BACKEND


### Linux System

#### Install

```shell
pip install --upgrade pip setuptools
pip install -r requirements.txt
```

#### Run

```shell
gunicorn --bind 127.0.0.1:8000 auxiliarLogistica.app
```

### Windows System

#### Install

```shel
pip install --upgrade pip setuptools
pip install -r requirements.txt
pip install waitress
```

#### Run

```shel
waitress-serve --listen=*:8000 sistema.wsgi:application
```


## FRONTEND

### Install

```bash
npm install
```

```bash
npm start
```

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

```bash
npm test
```

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

```bash
npm run build
```

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.