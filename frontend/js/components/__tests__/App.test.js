import Adapter from 'enzyme-adapter-react-16';
import axios from 'axios';
import Enzyme, { shallow } from 'enzyme';
import { mount } from 'enzyme';
import React from 'react';
// import Api from '../../Api';
import App from '../App.react';
import ContactForm from '../ContactForm.react';

jest.mock("../Api")

Enzyme.configure({adapter: new Adapter()});

describe('App', () => {
  const app = shallow(<App />);

  it('renders correctly', () => {
    expect(app).toMatchSnapshot();
  });

  it('initializes the states with contacts fetched with Api.getContacts()', () => {
    expect(app.state().contacts).toEqual([{
      name: "Justyna",
             telephone: "111111",
             id: 1
    },
    {
      name: "kosia",
             telephone: "222",
             id: 2
    }]);
  });

  describe('displaying contacts on the website using data from mock fetch', () => {
    it('has contacts on the website from fetch', () => {
      expect(app.find('.contacts-list').children().length).toEqual(2);
    })
  })

  describe('adding new contacts to the website', () => {
    const appParent = mount(<App />)

    beforeEach(() => {
      appParent.find('.input-name').hostNodes().simulate('change', { target: { value: "Kosinka"}});
      appParent.find('.input-phone').hostNodes().simulate('change', { target: { value: "5555"}});
      appParent.find('.btn-add').hostNodes().simulate('click');
    });

    it('has contacts on the website after adding', () => {
      expect(appParent.find('ContactForm').exists())
      expect(appParent.exists('.input-phone')).toEqual(true);
      appParent.update()
      expect(appParent.find('.contacts-list').children().length).toEqual(3);
    })
  })
})
