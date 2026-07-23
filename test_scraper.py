import pytest
from unittest.mock import patch, MagicMock
from main import LinkedInScraper

@patch("main.check_internet", return_value=True)
@patch("main.requests.get")
def test_scrape_url_success(mock_get, mock_check_internet):
    # Setup mock HTML response
    html_content = """
    <html>
        <body>
            <h1 class="top-card-layout__title">Test Company Name</h1>
            <p class="about-us__description">Test Bio Description</p>
            <a class="about-us__link" href="https://www.testcompany.com">Test Website</a>
            <div class="top-card-layout__first-subline">San Francisco, CA</div>
            <dl>
                <dt>Founded</dt>
                <dd>2010</dd>
            </dl>
        </body>
    </html>
    """
    mock_response = MagicMock()
    mock_response.text = html_content
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    result = LinkedInScraper.scrape_url("https://www.linkedin.com/company/test")
    
    assert result["name"] == "Test Company Name"
    assert result["bio"] == "Test Bio Description"
    assert result["website"] == "testcompany.com"
    assert result["location"] == "San Francisco, CA"
    assert result["founded"] == "2010"
    assert result["status"] == "completed"
    assert result["error"] is None
    assert result["url"] == "https://www.linkedin.com/company/test"

@patch("main.check_internet", return_value=True)
@patch("main.requests.get")
def test_scrape_url_http_error(mock_get, mock_check_internet):
    mock_response = MagicMock()
    mock_response.status_code = 429
    mock_response.text = "Too Many Requests"
    mock_response.raise_for_status.side_effect = Exception("HTTP 429")
    mock_get.return_value = mock_response

    result = LinkedInScraper.scrape_url("https://www.linkedin.com/company/test")
    
    assert result["status"] == "error"
    assert result["error"] is not None
