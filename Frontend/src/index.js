import React from 'react';
import ReactDOM from 'react-dom';

import { Provider } from "react-redux";
import store from "./store"

import App from './components/App';

import "mdb-ui-kit"

// Bundle custom javascript files
import "./static/js/bundle"
// Bundle custom Sass files
import "./static/scss/bundle.scss"

import * as serviceWorker from './serviceWorker';

ReactDOM.render(
  <Provider store={store}>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </Provider>,
  document.getElementById('root')
);

serviceWorker.unregister();
