import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import { withStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import TranslationArea from '../components/TranslationArea';
import NavButton from '../components/NavButton';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';
import BottomNav from './BottomNav';

const drawerWidth = 400;

const styles = theme => ({
  root: {
    display: 'flex',
  },
  appBar: {
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  appBarShift: {
    width: `calc(100% - ${drawerWidth}px)`,
    marginLeft: drawerWidth,
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  menuButton: {
    marginLeft: 12,
    marginRight: 20,
  },
  hide: {
    display: 'none',
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
  },
  drawerPaper: {
    width: drawerWidth,
  },
  drawerHeader: {
    display: 'flex',
    alignItems: 'center',
    padding: '0 8px',
    ...theme.mixins.toolbar,
    justifyContent: 'flex-end',
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing.unit * 3,
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    marginLeft: -drawerWidth,
  },
  contentShift: {
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
    marginLeft: 0,
  },
});



class Home extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      open: false,
      screen: 'Text',
      textInput: '',
      inputLang: '',
      outputLang: '',
      languages: ["English", "Japanese", "Vietnamese"],
      langValues: {
        input: -1,
        output: -1,
      },
    };
  }

  handleDrawerOpen = () => {
    this.setState({ open: true });
  };

  handleDrawerClose = () => {
    this.setState({ open: false });
  };


  changeTextInput = (textInput) => {
    this.setState({textInput})
  }

  changeInputLang = (inputLang) => {
    this.setState({
      inputLang,
      langValues: {
        input: this.state.languages.indexOf(inputLang),
        output: this.state.langValues.output
      }
    })
  }

  changeOutputLang = (outputLang) => {
    this.setState({
      outputLang,
      langValues: {
        input: this.state.langValues.input,
        output: this.state.languages.indexOf(outputLang)
      }
    })
  }

  changeScreen= (screen) => {
    this.setState({screen})
  }

  swapLang = () => {
    let inputLang = this.state.inputLang
    let outputLang = this.state.outputLang
    this.setState({
      inputLang: outputLang,
      outputLang: inputLang,
      langValues: {
        output: this.state.languages.indexOf(inputLang),
        input: this.state.languages.indexOf(outputLang)
      }
    })
  }

  render() {
    const { classes, theme } = this.props;
    const { open } = this.state;

    return (
      <div className={classes.root}>
        <CssBaseline />
        <AppBar
          position="fixed"
          className={classNames(classes.appBar, {
            [classes.appBarShift]: open,
          })}
        >
          <Toolbar disableGutters={!open}>
            <IconButton
              color="inherit"
              aria-label="Open drawer"
              // onClick={this.handleDrawerOpen}
              className={classNames(classes.menuButton, open && classes.hide)}
            >
              <MenuIcon />
            </IconButton>
            <Typography variant="h6" color="inherit" noWrap>
              Translator
            </Typography>
          </Toolbar>
        </AppBar>
        <Drawer
          className={classes.drawer}
          variant="persistent"
          anchor="left"
          open={open}
          classes={{
            paper: classes.drawerPaper,
          }}
        >
          <div className={classes.drawerHeader}>
            <IconButton onClick={this.handleDrawerClose}>
              {theme.direction === 'ltr' ? <ChevronLeftIcon /> : <ChevronRightIcon />}
            </IconButton>
          </div>
        </Drawer>
        <main
          className={classNames(classes.content, {
            [classes.contentShift]: open,
          })}
        >
           <div className={classes.drawerHeader} />
          <NavButton changeScreen={this.changeScreen}/>
          <TranslationArea
            changeInputLang={this.changeInputLang}
            changeOutputLang={this.changeOutputLang}
            changeTextInput={this.changeTextInput}
            languages={this.state.languages}
            inputLang={this.state.inputLang}
            textInput={this.state.textInput}
            screen={this.state.screen}
            swapLang={this.swapLang}
            langValues={this.state.langValues}
            text={this.state.textInput}
            />
            <BottomNav openSide={this.handleDrawerOpen}/>
        </main>
      </div>
    );
  }
}

Home.propTypes = {
  classes: PropTypes.object.isRequired,
  theme: PropTypes.object.isRequired,
};

export default withStyles(styles, { withTheme: true })(Home);
