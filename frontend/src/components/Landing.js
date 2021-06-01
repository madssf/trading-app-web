// frontend/src/components/Home.js

import React, { Component } from "react";
import { Link } from "react-router-dom";
import { Container } from "react-bootstrap";

class Landing extends Component {
  render() {
    return (
      <Container>
        <h1>Trading App Web</h1>
        <p>
          <Link to="/login/">Login</Link>
        </p>
        <p>
          <Link to="/signup">Sign up</Link>
        </p>
        <p>
          <Link to="/home">Home</Link>
        </p>
      </Container>
    );
  }
}

export default Landing;