import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Button, Form } from "react-bootstrap";
import { addTag } from "./TagsActions";

class AddTag extends Component {
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
    const tag = {
      name: this.state.name,
      description: this.state.description
    };
    this.props.addTag(tag);
  };

  render() {
    return (
      <div>
        <h2>Add new tag</h2>
        <Form>
        <Form.Group controlId="nameId">
            <Form.Label>Name</Form.Label>
            <Form.Control
              as="textarea"
              rows={3}
              name="name"
              placeholder="Enter tag name"
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
              placeholder="Enter tag description"
              value={this.description}
              onChange={this.onChange}
            />
          </Form.Group>
        </Form>
        <Button variant="success" onClick={this.onAddClick}>
          Add tag
        </Button>
      </div>
    );
  }
}

AddTag.propTypes = {
  addTag: PropTypes.func.isRequired
};

const mapStateToProps = state => ({});

export default connect(mapStateToProps, { addTag })(withRouter(AddTag));