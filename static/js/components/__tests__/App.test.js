import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
// import fetch from 'isomorphic-fetch'
import { mount } from 'enzyme';
// import sinon from 'sinon';
import axios from 'axios';

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

  describe('when there are some contacts in the state', () => {
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

  describe('when adding a contact', () => {

    // const contactFormComponent = mount(
    //   <ContactForm onAddContact={addContactMock} />
    // );
    //
    // beforeEach(() => {
    //   contactFormComponent.find('.input-name').hostNodes().simulate('change', { target: { value: "Justyna"}});
    //   contactFormComponent.find('.input-phone').hostNodes().simulate('change', { target: { value: "111"}});
    //   contactFormComponent.find('.btn-add').hostNodes().simulate('click');
    // });
    //
    // afterEach(() => {
    //   app.setState({contacts: []});
    // })
    //
    // it('adds a new contact to the state', () => {
    //   const resp = {data: [{name: 'Justyna', telephone: "111"}]};
    //   axios.post.mockResolvedValue(resp);
    //
    //   expect(app.state().contacts.length).toEqual(1);
    // });
  });
});
