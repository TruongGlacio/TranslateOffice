import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Icon from '@material-ui/core/Icon';

const styles = theme => ({
  root: {
    flexGrow: 1,
    textAlign: 'center',
  },

  verticalLine: {
    borderLeft: `2px solid ${theme.palette.divider}`,
  },

  GridItem: {
    padding: 20,
  },

  input: {
    display: 'none',
  },

  button: {
    margin: theme.spacing.unit,
  },
});


class UploadArea extends Component {
  constructor(props) {
    super(props);
    this.classes = this.props.classes;
    this.state = {
      chosen: '',
    }
  }

  handleChange = (e) => {
    this.setState({
      chosen: e.target.value.replace('C:\\fakepath\\', '')
    })
  }

  render() {
    return (
      <div className={this.classes.root}>
        <Typography variant='h5' component='h3'>
          Choose a document.
        </Typography>
        <br/>
        <Typography component='p'>
          {this.state.chosen === '' ? 'No file chosen' : this.state.chosen}
        </Typography>
        <br/>
        <form action=''>
          <input
            accept='text/*'
            multiple
            id='contained-button-file'
            className={this.classes.input}
            type='file'
            onChange={this.handleChange}
          />
          <label htmlFor='contained-button-file'>
            <Button variant='contained' component='span' className={this.classes.button}>
              <Icon>attachment</Icon>
              Browse your computer
            </Button>
          </label>
          { this.state.chosen !== '' &&
            <Button type='submit' variant='contained' color='primary'>
              <Icon>cloud_upload</Icon>
              Submit
            </Button>
          }
        </form>
      </div>
    );
  }
}


UploadArea.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(UploadArea);
