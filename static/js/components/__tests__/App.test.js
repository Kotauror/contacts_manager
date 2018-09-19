import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import fetch from 'isomorphic-fetch'
import { mount } from 'enzyme';
import sinon from 'sinon';

Enzyme.configure({adapter: new Adapter()});

import App from '../App.react';
import ContactForm from '../ContactForm.react';
import Api from '../Api';

describe('App', () => {
  const app = shallow(<App />);

  it('renders correctly', () => {
    expect(app).toMatchSnapshot();
  });

  it('initializes the states with an empty list of contacts', () => {
    expect(app.state().contacts).toEqual([]);
  });

  describe('when adding a contact', () => {

    const addContactMock = jest.fn();
    const contactFormComponent = mount(
      <ContactForm onAddContact={addContactMock} />
    );

    beforeEach(() => {
      const promise = new Promise((r) => r({ id: 200, name: "hoto", telephone: "321"}));
      sinon.stub(Api, 'getContacts').returns([promise]);
      sinon.stub(Api, 'addContact').returns(promise);
      contactFormComponent.find('.input-name').hostNodes().simulate('change', { target: { value: "Justyna"}});
      contactFormComponent.find('.input-phone').hostNodes().simulate('change', { target: { value: "111"}});
      contactFormComponent.find('.btn-add').hostNodes().simulate('click');
    });

    afterEach(() => {
      app.setState({contacts: []});
    })

    it('adds a new contact to the state', () => {
      expect(app.state().contacts.length).toEqual(1);
    });
  });
});
