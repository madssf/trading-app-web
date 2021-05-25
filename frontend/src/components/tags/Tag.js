import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { deleteTag, updateTag } from "./TagsActions";
import { Button } from "react-bootstrap";

class Tag extends Component {
  onDeleteClick = () => {
    const { tag } = this.props;
    this.props.deleteTag(tag.id);
  };
  render() {
    const { tag } = this.props;
    return (
      <div>
        <hr />
        <p>{tag.name} | {tag.description}</p>
        <Button variant="danger" size="sm" onClick={this.onDeleteClick}>
          Delete
        </Button>

      </div>
    );
  }
}

Tag.propTypes = {
  tag: PropTypes.object.isRequired
};
const mapStateToProps = state => ({});

export default connect(mapStateToProps, { deleteTag, updateTag })(
  withRouter(Tag)
);
