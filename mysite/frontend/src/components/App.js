import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import { HashRouter as Router, Route, Switch, Redirect } from 'react-router-dom';

//import MuiAlert from "@material-ui/lab/Alert";

//import 'bootstrap/dist/css/bootstrap.min.css';

import Header from './layout/Header';

import { Provider } from 'react-redux';
import store from '../store';

class App extends React.Component {
    render() {
        return (
            <Provider store={store}>
                <Header />
                <div>
                    <h1>Hello World</h1>
                </div>
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));
