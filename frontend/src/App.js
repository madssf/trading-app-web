import './App.css';
import React, { Component } from "react";
import Root from "./Root";
import { Route, Switch } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import requireAuth from "./utils/RequireAuth";
import LandingPage from "./components/ui/LandingPage";
import Signup from "./components/auth/signup/Signup";
import Login from "./components/auth/login/Login";
import Home from "./components/home/Home";
import CurrenciesList from "./components/pages/currencies/CurrenciesList";
import StrategiesList from './components/pages/strategies/StrategiesList';
import PortfolioDetail from './components/home/portfolios/PortfolioDetail'
import NavBar from "./components/ui/NavBar";

import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:1337";


class App extends Component {
  
  render() {
    return (
      <div className='app'>
        <Root> 
           <NavBar/>          
           <Switch>
            <div className="base">
            <Route exact path="/" component={LandingPage} />
            <Route path="/signup" component={Signup} />
            <Route path="/login" component={Login} />
            <Route path="/home" component={requireAuth(Home)}/>
            <Route path="/currencies" component={requireAuth(CurrenciesList)}/>
            <Route path="/strategies" component={requireAuth(StrategiesList)}/>

            <Route exact path="/portfolios/:id" component={requireAuth(PortfolioDetail)}/>
            </div>
            <Route path="*">404 - Not Found</Route>
          </Switch>

        </Root>
        <ToastContainer hideProgressBar={true} newestOnTop={true} />
      </div>
    );
  }
}

export default App;