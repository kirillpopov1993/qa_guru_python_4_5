from selene import browser, have, be
import os


def test_register(browser_config):
    link = 'https://demoqa.com/automation-practice-form'
    browser.open(link)
    browser.execute_script('document.querySelector("footer").remove()')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.execute_script('document.querySelector("#RightSide_Advertisement").remove()')
    browser.element('[id=firstName]').type('Kirill')
    browser.element('[id=lastName]').type('Popov')
    browser.element('[id="userEmail"]').type('soladef290@aosod.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').type('1234567891')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="0"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1993"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--002 react-datepicker__day--weekend"]').click()
    browser.element('#subjectsInput').should(be.blank).type('Computer Science').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + f'/cat.png')
    browser.element('[id="currentAddress"]').type('Nizhny Novgorod')
    browser.element("[id=state]").click()
    browser.element("[id=react-select-3-option-1]").click()
    browser.element("[id=city]").click()
    browser.element("[id=react-select-4-option-0]").click()
    browser.element('#submit').click()

# Проверка правильности заполнения полей
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tr').element_by_its('td', have.text('Student Name')).all('td')[1].should(have.text('Kirill Popov'))
    browser.all('tr').element_by_its('td', have.text('Student Email')).all('td')[1].should(
        have.text('soladef290@aosod.com'))
    browser.all('tr').element_by_its('td', have.text('Gender')).all('td')[1].should(have.text('Male'))
    browser.all('tr').element_by_its('td', have.text('Mobile')).all('td')[1].should(have.text('1234567891'))
    browser.all('tr').element_by_its('td', have.text('Date of Birth')).all('td')[1].should(
        have.text('02 January,1993'))
    browser.all('tr').element_by_its('td', have.text('Subjects')).all('td')[1].should(have.text('Computer Science'))
    browser.all('tr').element_by_its('td', have.text('Hobbies')).all('td')[1].should(have.text('Sports'))
    browser.all('tr').element_by_its('td', have.text('Picture')).all('td')[1].should(have.text('cat.png'))
    browser.all('tr').element_by_its('td', have.text('Address')).all('td')[1].should(
        have.text('Nizhny Novgorod'))
    browser.all('tr').element_by_its('td', have.text('State and City')).all('td')[1].should(
        have.text('Uttar Pradesh Agra'))
    browser.element('#closeLargeModal').click()
