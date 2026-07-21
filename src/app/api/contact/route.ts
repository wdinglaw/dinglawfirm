import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const data = await request.json();

  if (!data?.name || !data?.email || !data?.phone || !data?.matterType || !data?.description || !data?.urgency || !data?.acknowledgement) {
    return NextResponse.json({ message: "Please complete all required fields." }, { status: 400 });
  }

  const contactProviderConfigured =
    Boolean(process.env.CONTACT_PROVIDER_API_KEY) &&
    Boolean(process.env.CONTACT_PROVIDER_TO_EMAIL);

  if (!contactProviderConfigured) {
    return NextResponse.json(
      {
        message:
          "Form capture is enabled, but outbound delivery is not configured yet. Please call (408) 320-8182 or email contact@dinglawgroup.com.",
      },
      { status: 200 },
    );
  }

  // TODO: Integrate an email provider here (for example, Resend, SendGrid, or SMTP).
  // Example integration point:
  // 1) Validate payload and map fields to your template.
  // 2) Send to process.env.CONTACT_PROVIDER_TO_EMAIL.
  // 3) Log submission metadata securely and return a confirmation message.

  return NextResponse.json({ message: "Thank you. Your inquiry has been received." }, { status: 200 });
}
