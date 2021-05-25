import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { getTags } from "./TagsActions";

import Tag from "./Tag";
import axios from "axios";

class TagsList extends Component {
  componentDidMount() {
    this.props.getTags();
  }

  render() {
    const { tags } = this.props.tags;

    if (tags.length === 0) {
      return <p>No tags yet, but you can add one.</p>;
    }

    let items = tags.map(tag => {
      return <Tag key={tag.id} tag={tag} />;
    });

    return (
      <div>
        <h2>Tags</h2>
        {items}
        <hr />
      </div>
    );
  }


}

TagsList.propTypes = {
  getTags: PropTypes.func.isRequired,
  tags: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  tags: state.tags
});

export default connect(mapStateToProps, {
  getTags
})(withRouter(TagsList));