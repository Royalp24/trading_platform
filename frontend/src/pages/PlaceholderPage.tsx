interface PlaceholderPageProps {
  title: string;
}

export function PlaceholderPage({ title }: PlaceholderPageProps) {
  return (
    <section>
      <p className="text-sm text-muted-foreground">Platform foundation</p>
      <h1 className="mt-1 text-3xl font-semibold tracking-tight">{title}</h1>
      <div className="mt-8 rounded-lg border border-dashed border-border p-10 text-muted-foreground">
        This module is ready for its scoped implementation.
      </div>
    </section>
  );
}
