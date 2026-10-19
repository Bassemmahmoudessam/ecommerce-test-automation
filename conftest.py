import os
import allure
import pytest
from playwright.sync_api import Page


@pytest.fixture
def page(browser, request: pytest.FixtureRequest):
    context = browser.new_context(
        record_video_dir="test-results/videos/", viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()

    yield page

    report = getattr(request.node, "rep_call", None)
    failed = report is not None and report.failed

    # Capture screenshot before closing the page
    if failed:
        try:
            screenshot = page.screenshot(type="png")
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print(f"Screenshot error: {e}")

    # Get video path before closing
    video = page.video
    video_path = video.path() if video else None

    # Close context so video is finalized and saved
    page.close()
    context.close()

    # Attach finalized video to Allure
    if failed and video_path and os.path.exists(video_path):
        try:
            with open(video_path, "rb") as file:
                allure.attach(
                    file.read(),
                    name="Failure Video",
                    attachment_type=allure.attachment_type.WEBM,
                )
        except Exception as e:
            print(f"Video attachment error: {e}")
