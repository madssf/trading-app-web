import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Button, Form } from "react-bootstrap";
import { addPortfolio } from "./PortfoliosActions";

class AddPortfolio extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "",
      description: ""
    };
  }
  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  onAddClick = () => {
    const portfolio = {
      name: this.state.name,
      description: this.state.description
    };
    this.props.addPortfolio(portfolio);
  };

  render() {
    return (
      <div>
        <h2>Add new portfolio</h2>
        <Form>
        <Form.Group controlId="nameId">
            <Form.Label>Name</Form.Label>
            <Form.Control
              as="textarea"
              rows={3}
              name="name"
              placeholder="Enter portfolio name"
              value={this.name}
              onChange={this.onChange}
            />
          </Form.Group>
          <Form.Group controlId="descriptionId">
            <Form.Label>Description</Form.Label>
            <Form.Control
              as="textarea"
              rows={3}
              name="description"
              placeholder="Enter portfolio description"
              value={this.description}
              onChange={this.onChange}
            />
          </Form.Group>
        </Form>
        <Button variant="success" onClick={this.onAddClick}>
          Add portfolio
        </Button>
      </div>
    );
  }
}

AddPortfolio.propTypes = {
  addPortfolio: PropTypes.func.isRequired
};

const mapStateToProps = state => ({});

export default connect(mapStateToProps, { addPortfolio })(withRouter(AddPortfolio));