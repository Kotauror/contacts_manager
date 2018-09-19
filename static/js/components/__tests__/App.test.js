import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import fetch from 'isomorphic-fetch'
import { mount } from 'enzyme';
import sinon from 'sinon';

Enzyme.configure({adapter: new Adapter()});

import App from '../App.react';
import ContactForm from '../ContactForm.react';

describe('App', () => {
  const app = shallow(<App />);

  it('renders correctly', () => {
    expect(app).toMatchSnapshot();
  });

  it('initializes the states with an empty list of contacts', () => {
    expect(app.state().contacts).toEqual([]);
  });

//   describe('when adding a contact', () => {
//
//     const addContactMock = jest.fn();
//     const contactFormComponent = mount(
//       <ContactForm onAddContact={addContactMock} />
//     );
//
//     beforeEach(() => {
//       const resolved = new Promise((r) => r({ data: Array.from([{ 0: { description: 'desc' } }]) }));
//       sinon.stub(app, 'fetch').returns(resolved);
//       contactFormComponent.find('.input-name').hostNodes().simulate('change', { target: { value: "Justyna"}});
//       contactFormComponent.find('.input-phone').hostNodes().simulate('change', { target: { value: "111"}});
//       contactFormComponent.find('.btn-add').hostNodes().simulate('click');
//     });
//
//     afterEach(() => {
//       app.setState({contacts: []});
//     })
//
//     it('adds a new contact to the state', () => {
//       // sinon.stub(fetch, 'post').returns(resolved);
//
//       expect(addContactMock.mock.calls.length).toBe(1);
//
//
//       // expect(app.state().contacts.length).toEqual(1);
//     });
//
//   it('API test', async function() {
//     global.fetch = jest.fn().mockImplementation(() => {
//       var p = new Promise((resolve, reject) => {
//         resolve({
//           json:function(){
//             return {Id: 1}
//           }
//         })
//       })
//       return p;
//   })
//
//   const response=await Co
//
//
// });

});
