import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import { mount } from 'enzyme';
import axios from 'axios';
import App from '../App.react';
import ContactForm from '../ContactForm.react';
import Api from '../Api';

Enzyme.configure({adapter: new Adapter()});

describe('App', () => {
  const app = shallow(<App />);

  it('renders correctly', () => {
    expect(app).toMatchSnapshot();
  });

  it('initializes the states with an empty list of contacts', () => {
    expect(app.state().contacts).toEqual([]);
  });

  describe('operations on contacts - unit test', () => {
    const contact = {name: "Kota", telephone: "000"}

    beforeEach(() => {
      app.setState({contacts: []});
    });

    afterEach(() => {
      app.setState({contacts: []});
    })

    it('add contact to state', () => {
      app.instance().addContact(contact)

      expect(app.instance().state.contacts[0].name).toEqual("Kota")
    })

    it('removes contact from state', () => {
      app.instance().addContact(contact)
      app.instance().deleteContact(contact)

      expect(app.instance().state.contacts.length).toEqual(0)
    })

    it('edits the contact in state', () => {
      var editInfo = {
          'oldName': "Kota",
          'newName': "Jusia",
          'newPhone': "000000"
      }
      app.instance().addContact(contact)
      app.instance().editContact(editInfo)

      expect(app.instance().state.contacts.length).toEqual(1)
      expect(app.instance().state.contacts[0].name).toEqual("Jusia")
      expect(app.instance().state.contacts[0].telephone).toEqual("000000")
    })
  })

  describe('displaying contacts on the website', () => {
    beforeEach(() => {
      app.setState({contacts: [{name: "Kota", telephone: "000"}]});
    });

    afterEach(() => {
      app.setState({contacts: []});
    })

    it('has contacts on the website', () => {
      expect(app.find('.contacts-list').children().length).toEqual(1);
    })
  })

  describe('integration tests', () => {

    const appWithChildren = mount(<App />)

    beforeEach(() => {
      appWithChildren.find('.input-name').hostNodes().simulate('change', { target: { value: "Justyna"}});
      appWithChildren.find('.input-phone').hostNodes().simulate('change', { target: { value: "111"}});
      appWithChildren.find('.btn-add').hostNodes().simulate('click');
    });

    afterEach(() => {
      appWithChildren.setState({contacts: []});
    })

    // it('adds a new contact to the state', () => {
    //   expect(appWithChildren.state().contacts.length).toEqual(1);
    // });
  });
});
