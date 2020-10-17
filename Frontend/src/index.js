import React from 'react';
import ReactDOM from 'react-dom';

import App from './components/App';

import "./static/scss/style.scss"
import "./static/js/bundle.js"

import * as serviceWorker from './serviceWorker';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

serviceWorker.unregister();
