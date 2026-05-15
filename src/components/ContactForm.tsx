"use client";

import { FormEvent, useState } from "react";

type Status = "idle" | "success" | "error";

export default function ContactForm() {
  const [status, setStatus] = useState<Status>("idle");
  const [message, setMessage] = useState("");

  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setStatus("idle");
    setMessage("");

    const form = event.currentTarget;
    const data = Object.fromEntries(new FormData(form).entries());

    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      const result = (await response.json()) as { message?: string };

      if (!response.ok) {
        throw new Error(result.message || "Unable to submit form.");
      }

      setStatus("success");
      setMessage(result.message || "Request submitted.");
      form.reset();
    } catch (error) {
      setStatus("error");
      setMessage(error instanceof Error ? error.message : "Submission failed.");
    }
  }

  return (
    <form className="grid gap-5" onSubmit={onSubmit} noValidate>
      <div className="grid gap-5 md:grid-cols-2">
        <label className="grid gap-2 text-sm">
          Name
          <input name="name" required className="rounded border border-line bg-white px-3 py-2" />
        </label>
        <label className="grid gap-2 text-sm">
          Email
          <input type="email" name="email" required className="rounded border border-line bg-white px-3 py-2" />
        </label>
        <label className="grid gap-2 text-sm">
          Phone
          <input name="phone" required className="rounded border border-line bg-white px-3 py-2" />
        </label>
        <label className="grid gap-2 text-sm">
          Opposing party name
          <input name="opposingPartyName" className="rounded border border-line bg-white px-3 py-2" />
        </label>
        <label className="grid gap-2 text-sm">
          County
          <input name="county" required className="rounded border border-line bg-white px-3 py-2" />
        </label>
        <label className="grid gap-2 text-sm">
          Matter type
          <select name="matterType" required className="rounded border border-line bg-white px-3 py-2">
            <option value="">Select one</option>
            <option>Divorce</option>
            <option>Custody / Visitation</option>
            <option>Support</option>
            <option>Property Division</option>
            <option>DV Restraining Order</option>
            <option>Move-Away / Relocation</option>
            <option>Disclosures</option>
            <option>Settlement Agreement</option>
            <option>Other Family Law Matter</option>
          </select>
        </label>
      </div>

      <label className="grid gap-2 text-sm">
        Brief description
        <textarea name="description" required rows={5} className="rounded border border-line bg-white px-3 py-2" />
      </label>

      <label className="grid gap-2 text-sm md:max-w-xs">
        Urgency level
        <select name="urgency" required className="rounded border border-line bg-white px-3 py-2">
          <option value="">Select one</option>
          <option>Immediate (hearing or deadline within 7 days)</option>
          <option>Near-term (within 30 days)</option>
          <option>Standard (planning stage)</option>
        </select>
      </label>

      <label className="flex items-start gap-3 rounded border border-line bg-white p-3 text-sm">
        <input type="checkbox" name="acknowledgement" required className="mt-1" />
        <span>
          I understand that submitting this form does not create an attorney-client relationship.
        </span>
      </label>

      <button type="submit" className="w-fit rounded bg-ink px-5 py-3 text-sm font-semibold text-white transition hover:bg-mutedBlue">
        Submit Inquiry
      </button>

      {message ? (
        <p className={`text-sm ${status === "error" ? "text-red-700" : "text-green-700"}`}>{message}</p>
      ) : null}
    </form>
  );
}
